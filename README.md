# CeneoWebScraper

## Struktura opinii w serwisie [Ceneo.pl](https:///www.ceneo.pl/)

|Składowa|Selektor|Nazwa zmiennej|Typ zmiennej|
|--------|--------|--------------|------------|
|opinia|div.js_product-review|opinion|bs4.element.Tag|
|identyfikator opinii|div.js_product-review\["data-entry-id"\]|opinion_id|14133566|str|
|autor opinii|span.user-post__author-name|author|Maria|str|
|rekomendacje|span.user-post__author-recomendation  > em|recomendation|Polecam|str|
|liczba gwiazdek|span.user-post__score-count|stars|5/5|str|
|treść opinii|div.user-post__text|content|Lodówka amica jest warta zakupu|str|
|lista zalet|div.review-feature__title--positives ~ div.review-feature__item |pros|list|
|lista wad|div.review-feature__title--negatives ~ div.review-feature__item|conts|list|
|dla ilu osób przydatna|span[id^="votes-yes"]|useful|str|
|dla ilu osób nieprzydatna|span[id^="votes-no"]|useless|str|
|dla wystawienia mopinii|span.user-post__published > time:nth-child(1)["datetime"]|publish_date|str|
|data zakupu|span.user-post__published > time:nth-child(2)["datetime"]|purchase_date|str|

##Etapy pracy nad projektem
1. Pobranie do pojedynczych zmiennych składowych pojedynczej opinii
2. Zapisanie wszystkich składowych pojedynczej opinii do słownika
3. Pobranie wszystkich opiniii z pojedynczejstrony do słowników i zapisanie ich na liście
4. Zapisanie wszystkich opinii z listy do pliku .json
5. Pobranie wszystkich opinii o produkcie i zapisanie ich na liście w postaci słowników
6. Dodanie możliwośi podania kodu produktu przez użytkownika
7. Optymalizacja kodu
    a. utworzenie funkcji do ekstrakcji elementów strony
    b. utworzenie słownika selektorów
    c. użyce dictionary comprehension do pobrania składnych pojedynczych opinii na podstawie słownika selektorów 
8. Analiza pobranych opinii dla konkretnego produktu
    a. wyliczenie postwowych statystyk: 
        -liczba wszystkich opinii
        - liczba opinii dl aktórych podano zalety
        - liczba opinii dla których podano wady
        - średnia ocena produktu
    b. przygotowanie wykresów
        - udział poszczególnych rekoendacji w ogólnej liczbie opinii
        - histogram występowania poszczególnych ocen
9. Utworzenie strony o autorze
10. Wyświetlenie analizy danych produktów po podaniu przez użykownika kodu ów produku
11. Zapisanie poprzednio wyszukiwanych produktów i ich danych na liście na osobnej stronie
12. Zapisanie poprzednio wyszukiwanych produktów i ich danych w  postaci słownika
13. Aktualizaja pliku README.md 
14. Przeniesienie zawartości pliku README.md na stronę w formie zinterpretowanej



##Użyte Biblioteki##
- requests - Sluży do obsługi HTTP, wysyła żądania i odbiera odpowiedzi.
- json - Służy do wymiany danych, ich zapiu i odczytu w prosty i przerzysty sposób.
- pandas - Służy do analizy dnych. Możn je modyfikowa, wczytywać, czyścić, a przede wszystkim właśnie analizwać.
- numpy - Służy do analzy danych, głównie operacjach na macierzach, taki pakiet z obliczeniami naukowymi.
- bs4 - Służy do iteracji, wyszukiwania i modyfikacji kodu HTML i XML.
- flask - Służy do tworzenia aplikacji webowych.
- Markdown - Służy do konwersji formatu R.Markdown na inne formaty do HTML i XHTML.
- matplotlib - Służy do tworzenia różnych wykresów, bazujących na podanych danych.
- flask - Służy do debugowania oraz jest mikro-frameworkiem da Pythona.
