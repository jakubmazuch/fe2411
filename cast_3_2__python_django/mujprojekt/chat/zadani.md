# Chatovací aplikace přes společné rozhraní

## Úterý
1. Vytvořte na cestě ``/chat/`` místo pro zobrazení zpráv a formulář pro odeslání zprávy.
2. Přidejte 1 input a 2 tlačítka 
    - input a tlačítko pro odeslání zprávy
    - tlačítko pro načtení zpráv ze serveru
3. Přidejte na tlačítka naslouchač pomocí ``.addEventListener()`` (musíte prvku přiřadit ID ``#send-button``)

## Čtvrtek
4. Implementujte funkci pro načtení zpráv ze serveru do naslouchače
    - použijte JS funkci ``fetch(URL)`` (z FetchAPI) a pomocí ``.then()`` vypište zprávu do okna pro chat (element ``#chat-body``)
5. Implementujte funkci pro odesílání zpráv na server do naslouchače
    - získejte obsah zprávy z inputu (přiřaďme mu např. ID ``#chat-input``)
    - obsah zprávy pomocí ``fetch(URL, {method: POST, body: ...})`` odešlete na server. Obsah zprávy by měl být odeslán v "body: ..." (místo "..." :) )
6. Dodejte chatu scrollbar pomocí CSS (``overflow-y: scroll;``)
7. Přidejte automatickou aktualizaci chatu pomocí opakovače ``setInterval(FUNKCE_PRO_AKTUALITACI_CHATU, CAS_V_MILISEKUNDACH)``
