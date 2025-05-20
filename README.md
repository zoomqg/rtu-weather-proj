# Outfit Suggester

Šis projekts ir skripts, kas palīdz ātri izvēlēties apģērbu, veicot šādu pieprasījumu ciklu:

1. **Google Geocode API**: Norādītās vietas koordinātu iegūšana. (Lai strādātu, failā `.env` projekta mapē jānorāda `GOOGLE_GEOCODE_KEY`.)

2. **Open-Meteo API**: Informācijas par laikapstākļiem visas dienas garumā iegūšana.

3. **OpenRouter API**: Modeļa `llama-3.3-8b` izmantošana, lai sniegtu apģērbu ieteikumus trīs dienas daļām (rīts, diena, vakars). (Lai strādātu, failā `.env` projekta mapē jānorāda `OPENROUTE_KEY`.)

Pēdējo trīs pieprasījumu rezultāti tiek saglabāti JSON failā. Tā saturu var arī uzreiz izvadīt konsolē.

## Demonstrācija


https://github.com/user-attachments/assets/e6608833-ecac-4e06-8236-4c7fcb37da91



https://github.com/user-attachments/assets/ab2ac554-02de-40e5-b172-dca508d52154




## Atkarības

Galvenās bibliotēkas:
- `python-dotenv`
- `requests`

Pilns atkarību saraksts ir aprakstīts failā `requirements.txt`.

## Uzstādīšana un palaišana

1. Izveidojiet virtuālo vidi (pēc izvēles):
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/MacOS
   venv\Scripts\activate     # Windows
   ```

2. Instalējiet atkarības:
   ```bash
   pip install -r requirements.txt
   ```

3. Palaidiet projektu:
   ```bash
   python main.py
   ```

## Datu glabāšana

Informācija par pēdējiem trim pieprasījumiem tiek saglabāta JSON failā. Datu apstrādei tiek izmantotas hash tabulas (HashTables). Hash tabulu koda paraugs ir ņemts [šeit](https://www.geeksforgeeks.org/implementation-of-hash-table-in-python-using-separate-chaining/) un pielāgots projekta vajadzībām.

Pēc rezultātu apskates lietotājam tiek piedāvāta iespēja apskatīt pēdējos trīs pieprasījumus (ieskaitot pašreizējo).
