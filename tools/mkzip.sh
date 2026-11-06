set -e
S=/root/site/stage; rm -rf $S; mkdir -p $S; cd /home/claude/josons_site
cp -r admin.html _worker.js img pdf $S/
cp /root/site/seo/robots.txt /root/site/seo/sitemap.xml /root/site/seo/llms.txt $S/
{ printf '<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n'; cat index.html; printf '\n</body>\n</html>\n'; } > $S/index.html
rm -f /mnt/user-data/outputs/josons_upload.zip
(cd $S && zip -qr /mnt/user-data/outputs/josons_upload.zip index.html admin.html _worker.js robots.txt sitemap.xml llms.txt img pdf)
ls -l /mnt/user-data/outputs/josons_upload.zip
