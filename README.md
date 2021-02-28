# NYJC Timetable Parser

A timetable parser for NYJC. Outputs to `json` or `ics`.

# Usage

Clone the repo
```
git clone https://github.com/recreationx/nyjctimetable.git
```
Install Python (Built on Python 3.9.2) and required libraries. (`BeautifulSoup4`)
```
pip install -r requirements.txt
```
Run `timetableparse.py`
```
python timetableparse.py [filename] [outputname] [--type]
```
where `filename` is your HTML filename (`sample.html`, `sample.htm`) and `outputname` is the name of your `outputname.json` file <br>
`--type` (`json` or `ics`) will default to JSON if not specified.

## Note: Your `index_ex.php` is required as your HTML file.
Save your index_ex.php (timetable page) as a .html/htm from [NYXchange](https://nanyangjc.org/nyapps/timetable/) after logging in.

# Output
## ICS
A Calendar (.ics) file (universal calendar format) will be generated with the timezone set as `Asia/Singapore` (GMT+8).<br>
This can be used for importing into various calendar programs (Google Calendar etc.)
## JSON
Output file will be a `.json` file, in the following format. Sample is truncated to avoid sensitive information leak. <br>
`...` signifies that there are more entries. Lessons without a specified venue automatically defaults to `'NIL'`.

```json
{
    "Mon A": [
        {
            "name": "No Lesson",
            "venue": "NIL",
            "time": "0730-0800"
        },
        {
            "name": "No Lesson",
            "venue": "NIL",
            "time": "0800-0830"
        },
        {
            "name": "J2 Assembly",
            "venue": "NIL",
            "time": "0830-0900"
        },
        {
            "name": "gp",
            "venue": "5-34",
            "time": "0900-0930"
        },
        ...
    ],
    "Tue A": [
        {
            "name": "No Lesson",
            "venue": "NIL",
            "time": "0730-0800"
        },
        ...
    ]
}
```

# Disclaimer

Does not include tutor names to prevent sensitive information leak.
    
