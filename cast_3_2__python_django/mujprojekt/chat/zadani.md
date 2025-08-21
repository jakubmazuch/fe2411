# Chatovací aplikace přes společné rozhraní

## Úterý - příprava projektu, opakování JS
1. Vytvořte na cestě ``/chat/`` místo pro zobrazení zpráv a formulář pro odeslání zprávy.
2. Přidejte 1 input a 2 tlačítka 
    - input a tlačítko pro odeslání zprávy
    - tlačítko pro načtení zpráv ze serveru
3. Přidejte na tlačítka naslouchač pomocí ``.addEventListener()`` (musíte prvku přiřadit ID ``#send-button``)

## Čtvrtek - implementace frontendu chatu
4. Implementujte funkci pro načtení zpráv ze serveru do naslouchače
    - použijte JS funkci ``fetch(URL)`` (z FetchAPI) a pomocí ``.then()`` vypište zprávu do okna pro chat (element ``#chat-body``)
5. Implementujte funkci pro odesílání zpráv na server do naslouchače
    - získejte obsah zprávy z inputu (přiřaďme mu např. ID ``#chat-input``)
    - obsah zprávy pomocí ``fetch(URL, {method: POST, body: ...})`` odešlete na server. Obsah zprávy by měl být odeslán v "body: ..." (místo "..." :) )
6. Dodejte chatu scrollbar pomocí CSS (``overflow-y: scroll;``)
7. Přidejte automatickou aktualizaci chatu pomocí opakovače ``setInterval(FUNKCE_PRO_AKTUALITACI_CHATU, CAS_V_MILISEKUNDACH)``

## Úterý - implementace vlastního backendu
8. Implementujte GET metodu na cestě ``/chat/api`` pro výpis zpráv
    - definujte model ``Message``
    - vytvořte stránku s URL
    - Pomocí HTML vypište modely ``Message`` na danou cestu.
9. Implementujte POST metodu na cestě ``/chat/api``, která uloží obsah POSTu do databáze
10. Původní aplikace s fetchAPI propojte s naším novým ``/chat/api``
    - nahraďte URL adresu u načítání zpráv za naši novou ``http://localhost:8000/chat/api``
    - nahraďte URL adresu n odesílání zpráv za naši novou ``http://localhost:8000/chat/api``
    - přidejte do ``fetch`` u odesílání CSRF token (hlavička ``X-CSRFToken``) (bohužel platný jen na 1 odeslání (zatím))
    - JavaScriptem vytvořte formulář, přiřaďte hodnotě ``message`` obsah ``chat-input``
    - formulář vytvořený JS přidejte do ``body`` při odesílání přes ``fetch``

## Čtvrtek - implementace mazače zakázaných slov
11. Implementujte mazač zakázaných slov při eventu ``keyup`` v inputu chatu
    - definujte pole zakázaných slov, pokud naleznete zakázané slovo, vyhoďte ``alert()`` (zatím)
    - přepište kód, aby když bude slovo nalezeno, smaže se celý input (zatím)
    - nahraďte znaky jako ``$`` nebo ``@`` za jejich zaměňované znaky (najdete tím např. i ``a$$`` (angl. slovo ``ass``) apod.)
    - nahraďte všechny výskyty zakázaných slov v inputu hvězdičkami - ``***`` (``.replaceAll()``)
    - najděte první výskyt zakázaného slova a nahraďte pouze jej hvězdičkami (a přitom zanechte původní znaky ``$``, ``@``)
    - najděte všechny výskyty zakázaného slova a nahraďte stejným počtem hvězdiček, jako je délka slova (místo ``olovo`` -> ``*****``, ``popokatepetl`` -> ``************``)


# Doporučená dokumentace
- [https://developer.mozilla.org/en-US/docs/Web/API/EventTarget/addEventListener](Mozilla MDN - addEventListener())
- [https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Scripting/Events](Mozilla MDN - Learn addEventListener())
- [https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Scripting/Event_bubbling](Mozilla MDN - clickable events)