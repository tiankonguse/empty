
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
	printf("pkg len:%d iBufLen:%d offset:%d\n%s\n", iLen, iBufLen, offset, sHexBuf);
	return;
}


int main(int argc, char ** argv) {
	return 0;
}

