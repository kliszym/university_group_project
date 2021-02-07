#cleaning
rm -r APs
rm -r APs_tests
rm -r result
rm -r result_tests
#rebuilding
mkdir APs
mkdir APs_tests
mkdir result
mkdir result_tests
#prepare environment
python3 -m venv .
.\Scripts\activate
pip install -r requirements.txt
#run scripts
python sort_by_ap.py
python make_csv.py

python prepare_test_data.py
python make_csv_tests.py
#end
deactivate