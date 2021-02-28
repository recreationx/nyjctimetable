# NYJC Timetable Parser

A timetable parser for NYJC.

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
python timetableparse.py [filename] [outputname]
```
where `filename` is your HTML filename (`sample.html`, `sample.htm`) and `outputname` is the name of your `outputname.json` file

# Output

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
    
