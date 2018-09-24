### Projenin indirilmesi
- git clone https://github.com/tncyclk/lider-ahenk-update-version.git

### Bağımlılıkların Yüklenmesi
- pip3 install ezodf
- sudo apt install python3-git
- pip3 install lxml

### Konfigürasyonların Yapılması
- Version yükseltilecek eklentiler belirlenir.
- Eklentilerin hanli lider versiyonu ile çalışacağı belirlenir.
- Belirlenen versyion değerlerine göre conf dizini altında bulunan plugin_version.ods dosyası düzenlenir. Bu dosyada desteklenen lider versiyonu eklentinin versioyonu aynı olmadk sorunda değildir.


### Uygulamanın Çalıştırılması
- python3 setup.py

Uygulama sonucunda packages dizini altında eklentilere ait jar, deb ve zip paketlerini bulabilirsiniz.
