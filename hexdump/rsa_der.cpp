
#include <string>

using namespace std;

#define COL_TITLE "______00_01_02_03_04_05_06_07_08_09_0A_0B_0C_0D_0E_0F\n"

int HexDumpStr(const char *data, long size, unsigned char *sOutStr) {
	long i = 0;
	long x = 0;
	int isNotEnd = 1, offset = 0, len = 0;
	char d[32];
	unsigned char bfr[64];

	for (i = 0, x = 0;; i++) {
		if (i < size) {

			//当前行第一个, 加前缀
			if (x == 0) {
				len = snprintf((char*) &(sOutStr[offset]), 6 + 1, "%04lx: ", i);
				offset += len;
			}

			//输出16进制数据
			snprintf(d, 8 + 1, "%08x", data[i]);
			len = snprintf((char*) &(sOutStr[offset]), 3 + 1, "%c%c ", d[6],
					d[7]);
			offset += len;

			//明文转义
			bfr[x] = data[i];
			if (bfr[x] < 0x20) {
				bfr[x] = '.';
			}

			if (bfr[x] > 0x7f) {
				bfr[x] = '.';
			}

		} else {
			if (x == 0)
				break;
			else {
				len = snprintf((char*) &(sOutStr[offset]), 3 + 1, "   ");
				offset += len;
				bfr[x] = ' ';
				isNotEnd = 0;
			}
		}

		x++;
		if (!(x < 16)) {
			bfr[x++] = 0;
			len = snprintf((char*) &(sOutStr[offset]), x + 1, "%s\n", bfr);
			offset += len;
			x = 0;
			if (!isNotEnd)
				break;
		}
	}
	sOutStr[offset] = '\0';
	return offset;
}
void LogBufInfo(const char *sOutBuf, int iLen) {

	static unsigned char sHexBuf[1000000];
	int iBufLen = 0;

	if (iLen > 20000) {
		iBufLen = 20000;
	} else {
		iBufLen = iLen;
	}
	snprintf((char*) sHexBuf, sizeof(sHexBuf), "%s", COL_TITLE);
	int offset = HexDumpStr(sOutBuf, iBufLen, sHexBuf + strlen(COL_TITLE));
	printf("pkg len:%d iBufLen:%d offset:%d\n%s\n", iLen, iBufLen, offset,
			sHexBuf);
	return;
}

void LogBufInfo(std::string& key) {
	LogBufInfo(key.c_str(), key.length());
}

// Base64编码表：将输入数据流每次取6 bit，用此6 bit的值(0-63)作为索引去查表，输出相应字符。这样，每3个字节将编码为4个字符(3×8 → 4×6)；不满4个字符的以'='填充。
const char EnBase64Tab[] =
		"ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/";

// Base64解码表：将64个可打印字符的值作为索引，查表得到的值（范围为0-63）依次连起来得到解码结果。
// 解码表size为256，非法字符将被解码为ASCII 0
const char DeBase64Tab[] = { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
		0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
		0, 0,
		62,        // '+'
		0, 0, 0,
		63,        // '/'
		52, 53, 54, 55, 56, 57, 58, 59, 60,
		61,        // '0'-'9'
		0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14,
		15, 16, 17, 18, 19, 20, 21, 22, 23, 24,
		25,        // 'A'-'Z'
		0, 0, 0, 0, 0, 0, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38,
		39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50,
		51,        // 'a'-'z'
		0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
		0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
		0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
		0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
		0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
		0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };

string encode(const string &data, bool bChangeLine/* = false*/) {
	if (data.empty())
		return "";
	//设原始串长度为a,结果串中算上回车换行及'/0',最终长度为(a/3+1)*4+(a/3+1)*4*2/76+1,约为1.369*a+6
	char *pDst = NULL;
	int iBufSize = (int) (data.size() * 1.4) + 6;
	pDst = new char[iBufSize];
	if (pDst == NULL)
		return "";
	int iDstLen = encode((unsigned char*) data.c_str(), data.size(), pDst,
			bChangeLine);
	string ret(pDst, iDstLen);
	delete[] pDst;
	return ret;
}

string decode(const string &data) {
	if (data.empty())
		return "";
	unsigned char *pDst = NULL;
	pDst = new unsigned char[data.size()];
	if (pDst == NULL)
		return "";
	int iDstLen = decode(data.c_str(), data.size(), pDst);
	string ret((char*) pDst, iDstLen);
	delete[] pDst;
	return ret;
}

int encode(const unsigned char* pSrc, int nSrcLen, char* pDst,
		bool bChangeLine/* = false*/) {
	unsigned char c1, c2, c3;
	int nDstLen = 0;
	int nLineLen = 0;
	int nDiv = nSrcLen / 3;
	int nMod = nSrcLen % 3;
	// 每次取3个字节，编码成4个字符
	for (int i = 0; i < nDiv; i++) {
		c1 = *pSrc++;
		c2 = *pSrc++;
		c3 = *pSrc++;

		*pDst++ = EnBase64Tab[c1 >> 2];
		*pDst++ = EnBase64Tab[((c1 << 4) | (c2 >> 4)) & 0x3f];
		*pDst++ = EnBase64Tab[((c2 << 2) | (c3 >> 6)) & 0x3f];
		*pDst++ = EnBase64Tab[c3 & 0x3f];
		nLineLen += 4;
		nDstLen += 4;
		// 相关RFC中每行超过76字符时需要添加回车换行
		if (bChangeLine && nLineLen > 72) {
			*pDst++ = '\r';
			*pDst++ = '\n';
			nLineLen = 0;
			nDstLen += 2;
		}
	}
	// 编码余下的字节
	if (nMod == 1) {
		c1 = *pSrc++;
		*pDst++ = EnBase64Tab[(c1 & 0xfc) >> 2];
		*pDst++ = EnBase64Tab[((c1 & 0x03) << 4)];
		*pDst++ = '=';
		*pDst++ = '=';
		nLineLen += 4;
		nDstLen += 4;
	} else if (nMod == 2) {
		c1 = *pSrc++;
		c2 = *pSrc++;
		*pDst++ = EnBase64Tab[(c1 & 0xfc) >> 2];
		*pDst++ = EnBase64Tab[((c1 & 0x03) << 4) | ((c2 & 0xf0) >> 4)];
		*pDst++ = EnBase64Tab[((c2 & 0x0f) << 2)];
		*pDst++ = '=';
		nDstLen += 4;
	}
	// 输出加个结束符
	*pDst = '\0';

	return nDstLen;
}

int decode(const char* pSrc, int nSrcLen, unsigned char* pDst) {
	int nDstLen;            // 输出的字符计数
	int nValue;             // 解码用到的整数
	int i;
	i = 0;
	nDstLen = 0;

	// 取4个字符，解码到一个长整数，再经过移位得到3个字节
	while (i < nSrcLen) {
		// 跳过回车换行
		if (*pSrc != '\r' && *pSrc != '\n') {
			if (i + 4 > nSrcLen)                            //待解码字符串不合法，立即停止解码返回
				break;

			nValue = DeBase64Tab[int(*pSrc++)] << 18;
			nValue += DeBase64Tab[int(*pSrc++)] << 12;
			*pDst++ = (nValue & 0x00ff0000) >> 16;
			nDstLen++;
			if (*pSrc != '=') {
				nValue += DeBase64Tab[int(*pSrc++)] << 6;
				*pDst++ = (nValue & 0x0000ff00) >> 8;
				nDstLen++;
				if (*pSrc != '=') {
					nValue += DeBase64Tab[int(*pSrc++)];
					*pDst++ = nValue & 0x000000ff;
					nDstLen++;
				}
			}

			i += 4;
		} else {
			pSrc++;
			i++;
		}
	}
	// 输出加个结束符
	*pDst = '\0';
	return nDstLen;
}

void usage(char* exe) {
	printf("%s type key\n type: 0 public key; 1 private key");
}

int main(int argc, char ** argv) {
	if (argc != 3) {
		usage(argv[0]);
		return 0;
	}
	int type = atoi(argv[1]);
	std::string base64Key = argv[2];
	if (type == 0) {
		std::string binaryKey = decode(base64Key);
		LogBufInfo(binaryKey);
	}
