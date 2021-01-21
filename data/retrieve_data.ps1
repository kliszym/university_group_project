#cleaning
rm -r APs
rm result
#rebuilding
mkdir APs
mkdir result
#prepare environment
python3 -m venv .
.\Scripts\activate
pip install -r requirements.txt
#run scripts
python sort_by_ap.py
python make_csv.py
#end
deactivate