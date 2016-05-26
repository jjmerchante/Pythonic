cd /media/32gb
python gh-getPythonRepos.py > output1.txt 2>&1
echo "end 1" | mail -s "End 1" jj.merchante@gmail.com
cp -r json-repos /media/2/
cp gh-getPythonRepos.py /media/2/

cd /media/2
python gh-getPythonRepos.py > output2.txt 2>&1
echo "end 2" | mail -s "End 2" jj.merchante@gmail.com
cp -r json-repos /media/3/
cp gh-getPythonRepos.py /media/3/

cd /media/3
python gh-getPythonRepos.py > output3.txt 2>&1
echo "FIN TOTAL" | mail -s "FIN TOTAL" jj.merchante@gmail.com
