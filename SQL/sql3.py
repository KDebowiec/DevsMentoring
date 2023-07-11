# ACID to skrótowiec dla czterech fundamentalnych właściwości transakcji w systemach baz danych:
# Atomicity (Atomowość), Consistency (Spójność), Isolation (Izolacja) i Durability (Trwałość).
# Oto krótkie omówienie każdej z tych cech:
#
# Atomicity (Atomowość): Transakcje w bazach danych są atomowe, co oznacza, że są traktowane jako jedna, niepodzielna jednostka.
# Oznacza to, że wszystkie operacje w transakcji muszą zostać wykonane albo wszystkie, albo żadna.
# Jeśli wystąpi błąd podczas transakcji, to wszystkie wprowadzone zmiany zostaną wycofane, aby zachować spójność danych.
#
# Consistency (Spójność): Transakcje muszą przestrzegać zdefiniowanych reguł integralności danych,
# aby zapewnić spójność bazy danych. Oznacza to, że po zakończeniu transakcji baza danych powinna znajdować się w poprawnym,
# spójnym stanie zgodnym ze zdefiniowanymi regułami.
#
# Isolation (Izolacja): Każda transakcja powinna być izolowana od innych transakcji, tak aby jedna transakcja nie zakłócała
# działania innych. Zapewnienie izolacji oznacza, że transakcje muszą działać niezależnie od siebie,
# tak jakby były wykonywane sekwencyjnie.
#
# Durability (Trwałość): Po zakończeniu transakcji i zatwierdzeniu zmian, dane muszą być trwałe i niezależne
# od ewentualnych awarii systemu. Oznacza to, że po zatwierdzeniu transakcji, wprowadzone zmiany muszą być przechowywane
# trwale i odzyskiwalne nawet w przypadku awarii sprzętu lub oprogramowania.
#
# Co do związku z naszym Context Managerem i wykonywaniem zapytań w bloku with, używając takiej konstrukcji, możemy
# zapewnić automatyczne zarządzanie transakcjami w bazie danych. Kontekst zarządzany przez blok with gwarantuje, że
#     transakcja zostanie rozpoczęta na początku bloku with, a następnie zostanie zatwierdzona (commit) lub wycofana
#     (rollback) na końcu bloku with, niezależnie od tego, czy wystąpił błąd wewnątrz bloku. To zapewnia atomowość operacji i trwałość zmian.


# Zmiany w bazie danych są trwałe tylko wtedy, gdy wszystkie zapytania są wykonane poprawnie i nie zgłaszają wyjątków.
# W przypadku wystąpienia wyjątku, żadne zmiany nie zostaną utrwalone w bazie danych
#
# Jeśli w 4-tym z pięciu zapytań do bazy danych rzuci wyjątkiem, wykona się metoda rollback i żadne z zapytań nie wprowadzi
# zmian