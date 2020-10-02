# Apply core-nlp for tokenizer
`python tokenCRF.py`
`python tokenLongMatching.py`

# core-nlp
https://github.com/deepai-solutions/core_nlp

# Report

**** Lấy ra top 100 từ, note lại các rules, bổ sung stopword để loại các từ vô nghĩa/phổ thông
 - RULES: 
   + bỏ các từ không chứa các kí tự tiếng Việt
   + bỏ các số nhỏ hơn 100
   + bỏ các từ chỉ có 1 kí tự
   + bổ sung stopwords: cus_stopwords.txt
   + bổ sung bi-grams: việt_nam, trung_quốc, hàn_quốc, phân_khúc
 - METHODS:
   + chia ra làm top overall, top 2-word, top 1-word

**** Đánh giá top 20 sau cùng

FILE: ifollows.txt

 - Đánh giá 2 phương pháp:
 	* CRF
 		+ Cả file: 112781 kí tự => 1.18s
 		+ Nửa file: 50000 kí tự => 0.58s

 		=> Lợi: độ chính xác cao hơn, loại bỏ được nhiều nhập nhằng, có khả năng train tiếp
 		=> Nhược: thời gian chậm hơn (bao gồm cả thời gian load model)

 	* LongestMatching
 		+ Cả file: 112781 kí tự => 0.59s
 		+ Nửa file: 50000 kí tự => 0.28s
 		
 		=> Lợi: nhanh, không phải train, chỉ cần bộ từ điển đủ lớn
 		=> Nhược: không loại bỏ được hoàn toàn nhập nhằng, và không xử lý được khi gặp từ không có trong từ điển

 - Kết quả:
 	+ Top overall:
		#1. việt nam x364
		#2. giá x303
		#3. 2020 x168
		#4. mẫu x161
		#5. ra mắt x134
		#6. thị trường x132
		#7. nissan x129
		#8. kia x120
		#9. toyota x119
		#10. phân phối x119
		#11. 2021 x102
		#12. honda x86
		#13. đối thủ x73
		#14. baomoi x69
		#15. ciaz x69
		#16. kona x68
		#17. đại lý x67
		#18. suzuki x65
		#19. suv x59
		#20. chính thức x59

 	+ Top 1-word:
		#1. giá x303
		#2. 2020 x168
		#3. mẫu x161
		#4. nissan x129
		#5. kia x120
		#6. toyota x119
		#7. 2021 x102
		#8. honda x86
		#9. baomoi x69
		#10. ciaz x69
		#11. kona x68
		#12. suzuki x65
		#13. suv x59
		#14. tucson x57
		#15. lăn x55
		#16. morning x54
		#17. sedan x53
		#18. bánh x52
		#19. baonhanh247 x50
		#20. techz x48

 	+ Top 2-word:
		#1. việt nam x364
		#2. ra mắt x134
		#3. thị trường x132
		#4. phân phối x119
		#5. đối thủ x73
		#6. đại lý x67
		#7. chính thức x59
		#8. hàn quốc x54
		#9. phiên bản x50
		#10. phân khúc x49
		#11. giảm giá x46
		#12. có giá x42
		#13. phát triển x40
		#14. nâng cấp x38
		#15. cạnh tranh x36
		#16. công nghiệp x36
		#17. honda cr x34
		#18. doanh nghiệp x30
		#19. khách hàng x29
		#20. trở lại x28
