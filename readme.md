# AlgoritmaG Repository This repository includes 'Hello world' file and solution of problem. Bugünkü verilen soru ve yapılması gereken görev için python bilgim yetersiz kaldı ama araştıma ve denemelerle uygun çözümü bulduğumu düşünüyorum. Tam olarak Python ile bu şekilde alıştırma ya da soru çözümü hiç yapmamıştım, istatistik öğrencisi olarak veri setleri ile projeler yaptığım için bu tarz sorulara kendim direkt cevap bulmakta zorlanacağımı düşünüyorum. Teşekkürler.
Kullanacağımız indeksleri 0 olarak ayarlarız.
Metindeki her bir karakterin en son hangi indekste görüldüğünü izlemek 'char_to_index' oluştururuz.
'enumerate' fonksiyonu her bir karakter ve indeks çifti üzerine tekrarlarız.
Eğer şu anki alt dizi uzunluğu (i - start + 1) mevcut maksimum uzunluğu (max_len) aşarsa, bu yeni uzunluk ve alt dizi, ilgili değişkenlere atanır.
Döngü sona erdikten sonra, en uzun alt dizi (max_substring) ve uzunluğu (max_len) döndürülür.
inputla kullanıcıdan girdi alınarak longest_substring_without_duplicates çağırılar ekrana sonuç yazdırılır.
"input" olarak girilen metindeki en uzun tekrarsız alt dizi ve uzunluğu "output" olarak ekrana yazdırılır.

output;

$ python question.py
input: ABBCDDEFGHII
output: DEFGHI length: 6

$ python question.py
input: AABBCCD
output: AB length: 2

$ python question.py
input: ABCD
output: ABCD length: 4

