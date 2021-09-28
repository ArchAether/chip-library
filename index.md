# Description
---
chip-library is an api built in Python's Django that returns JSONs of battlechips found in Mega Man Battle Network 6. It uses a .csv file to store battlechip information, found in '/battlechips/static/csvs/MMBN6-BattleChips.csv'
# Endpoints:
---
|Name|Variable|Description|
| --- | --- | --- |
|/battlechips/|none|Returns a JSON list of all battlechips in Mega Man Battle Network 6|
|.../{id}/|int|Returns a JSON of the battlechip with id number {id}|
|.../{name}/|string|Returns a JSON of the battlechip with the same name as {name}|
|.../elem/{elem}/|string|Returns a JSON list of all battle chips with the same element as {elem}|
|.../code/{code}/|string|Returns a JSON list of all battlechips with the same code as {code}|
|.../class/{chipClass}/|string|Returns a JSON list of all battlechips with the same chip class as {chipClass}|
|.../version/{version}/|string|Returns a JSON list of all battlechips belonging to the version with the same name as {version}|
|.../desc/{description}/|string|Returns a JSON list of all battlechips with descriptions containing {description}|


# Links
---
[Back to the Home Page](https://archaether.github.io/)
