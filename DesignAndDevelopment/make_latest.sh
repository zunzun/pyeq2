zip -x "*.pyc" -x "*.svn*" -r pyeq2_latest.zip pyeq2/
tar --exclude=.svn* --exclude=*pyc -czvf pyeq2_latest.tgz pyeq2/
