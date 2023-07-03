from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

while True:
    try:
        # Selenium web sürücüsünü başlatmak için gerekli olan seçenekleri oluşturun
        options = webdriver.ChromeOptions()

        # Tarayıcıyı başsız (headless) modda çalıştırmak için seçeneği etkinleştirin
        options.headless = True

        # Selenium sürücüsünü oluşturun
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

        # Kullanıcıdan Twitch adını alın
        name = input("Twitch adınızı girin: ").lower()

        # URL'yi oluşturun
        url = f"https://fossabot.com/{name}/commands"

        # Tarayıcıda belirtilen URL'yi açın
        driver.get(url)

        # Tablo gövdesi elementinin sayfada görüntülenmesini bekleyin
        wait = WebDriverWait(driver, 10)
        table_body = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'MuiTableBody-root')))

        # Tablo gövdesi içindeki tüm satırları bulun
        rows = table_body.find_elements(By.TAG_NAME, 'tr')

        # Satırları döngüye alın
        for row in rows:
            # Mevcut satır içindeki tüm hücreleri bulun
            cells = row.find_elements(By.TAG_NAME, 'td')

            # İlk 2 hücreyi döngüye alın
            for i in range(2):
                # Hücrenin metnini alın ve ekrana yazdırın
                cell_text = cells[i].text
                print(cell_text)

            # Ayırıcı bir çizgi ekleyin
            print('-------------')

        # Sürücüyü kapatın
        driver.quit()

        # Döngüyü sonlandırın
        break

    except:
        print("Bulunamadı. Tekrar deneyin.\n")
