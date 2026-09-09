# Тест межсущностного обмена KOO → SHT

## Задача ШТАБИСТУ

Проверить адресную доставку через `wellbeing-hq` без ручной передачи файла ОПЕРАТОРОМ.

После получения locator:

1. прочитать именно указанную immutable-версию этого файла;
2. сверить путь и commit SHA с dispatch;
3. создать receipt по правилам Exchange Gate v1;
4. отдельно вернуть содержательный результат: `ACCEPTED`, если текст этого задания прочитан и версия совпала, иначе `REJECTED` с конкретной причиной.

Этот файл не вводит новых проектных норм и существует только как контрольный артефакт end-to-end теста транспортного контура.

## Служебное

- sender: koordinator
- recipient: shtabist
- document_type: exchange-e2e-test
- status: test-artifact
- project_time: omitted; trusted project-time source not used
