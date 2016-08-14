prefile="tmp_prefile"; 

printf "%10s  %20s\n" "cidNum" "当前文件专辑个数";
printf "%10s  %20s\n" "commonNum" "和上个文件专辑相同的个数";
printf "%10s  %20s\n" "delNum" "只在上个文件存在的专辑个数";
printf "%10s  %20s\n" "cidNum" "只在当前文件存在的专辑个数";
                   
printf  "%40s %10s %10s %10s %10s\n" "fileName" "cidNum" "commonNum" "delNum" "addNum";

for file in cover_info_143* ; do 
    cidNum=$(cat $file|wc -l);
    sumNum=$(cat $file $prefile|sort -u|wc -l);
    cat $file | sort -u > tmp_file;
    cat $prefile | sort -u > tmp_prefile;
    
    delNum=$(diff tmp_file tmp_prefile | grep ">" | wc -l);
    addNum=$(diff tmp_file tmp_prefile | grep "<" | wc -l);
    commonNum=$(($sumNum - $delNum - $addNum));
    printf "%40s %10s %10s %10s %10s\n" "$file" "$cidNum" "$commonNum" "$delNum" "$addNum";
    prefile=$file; 
done