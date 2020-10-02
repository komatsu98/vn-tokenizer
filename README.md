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



 - Đánh giá 2 phương pháp:
 	* CRF
 		FILE: ifollows.txt
 		+ Cả file: 112781 kí tự => 1.18s
 		+ Nửa file: 50000 kí tự => 0.58s

		FILE: social.txt
		+ Cả file: 443718 kí tự => 12.28s
 		+ Nửa file: 200000 kí tự => 10.13s

 	=> Lợi: độ chính xác cao hơn, loại bỏ được nhiều nhập nhằng, có khả năng train tiếp

 	=> Nhược: thời gian chậm hơn (bao gồm cả thời gian load model)

 	* LongestMatching
 		FILE: ifollows.txt
 		+ Cả file: 112781 kí tự => 0.59s
 		+ Nửa file: 50000 kí tự => 0.28s
 		
 		FILE: social.txt
		+ Cả file: 443718 kí tự => 9.75s
 		+ Nửa file: 200000 kí tự => 8.11s

 	=> Lợi: nhanh hơn (không đáng kể), không phải train, chỉ cần bộ từ điển đủ lớn

 	=> Nhược: không loại bỏ được hoàn toàn nhập nhằng, và không xử lý được khi gặp từ không có trong từ điển

 - Kết quả: results/ifollows.txt/
 	