🎬 Netflix Data Analysis — Exploratory Data Analysis Project

Bu proje, Netflix içerik veri seti üzerinde veri temizleme, keşifsel veri analizi (EDA), görselleştirme ve trend çıkarımı yapılmasını içerir.
Amaç, Netflix'in içerik stratejisini anlamaya yönelik içgörüler üretmektir.

📁 Proje Yapısı
Netflix-Data-Analysis/
│
├── data/
│   └── netflix_titles.csv
│
├── notebooks/
│   └── netflix_analysis.ipynb
│
├── src/
│   ├── cleaning.py
│   ├── eda.py
│   ├── visualize.py
│   └── utils.py
│
├── README.md
└── requirements.txt

🔧 Kullanılan Teknolojiler

Python

Pandas

NumPy

Seaborn

Matplotlib

Jupyter Notebook

🧼 Veri Temizleme (Data Cleaning)

Eksik verilerin doldurulması

date_added → datetime formatına dönüşüm

duration → sayısal değere (duration_int) dönüştürme

Süre tipi ayırma (duration_type)

country ve director boş değerlerinin "Unknown" yapılması

📊 Yapılan Analizler (EDA)

Movie vs TV Show dağılımı

Yayın yılı trend analizi

En çok içerik üreten ülkeler

Rating dağılımı

Tür analizleri

Tarihe göre eklenen içerik trendi

🔍 İçgörüler (Findings)

🎬 Netflix'te film sayısı, dizi sayısından fazladır.

📈 2015–2020 arası içerik üretiminde belirgin bir artış vardır.

🌍 En fazla içerik ABD ve Hindistan tarafından üretilir.

🔞 Rating kategorisinde TV-MA baskındır.

🎭 En popüler tür Dramadır.

📅 Eklenen içerik trendi yıllar içinde keskin şekilde yükselmiştir.

📦 Nasıl Çalıştırılır?
pip install -r requirements.txt
jupyter notebook


Notebook klasörü:

/notebooks/netflix_analysis.ipynb