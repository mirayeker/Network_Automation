
# Network Automation
Projemizin adından da anlaşılacağı üzere, bir ağdaki fiziksel veya sanal cihazların yönetimi, test edilmesi gibi network işlemlerini otomatikleştirmek amaçlanmıştır.





## Kullanılan Teknolojiler

**Python** , **VirtualBox** , **Flask** , **PostgreSQL** 

**Paramiko**, **SSH Protokolü**, **Ngork**   

  
## Açıklama

- VirtualBox'a 3 tane sanal makine kuruyoruz.
- Sanal makineler arasında SSH protokolü ve paramiko yardımıyla iletişim sağlıyoruz.
- Bağlandığımız makinelerdeki gerekli bilgilere (_ekte mevcut_) komutlarla ulaşıp veritabanımıza kaydediyoruz. 
- Flask ile api'leri oluşturup local'de çalışmasını sağlıyoruz.
- ngrok ile localden çıkarıp, web'e aktardık. 
- Flutter ile mobil tasarımını yapıyoruz. 


  
## Dağıtım

Bu projeyi dağıtmak için çalıştırın

```bash
  flask run
```

  
## Veritabanı

![Uygulama Ekran Görüntüsü](https://raw.githubusercontent.com/mirayeker/network_automation/master/veritabani_semasi.jpeg)

  
## Belgelendirme

[Sistem Tasarım Dökümanı (SDD)](https://github.com/mirayeker/network_automation/blob/master/sdd_networkautomation.pdf)

  
