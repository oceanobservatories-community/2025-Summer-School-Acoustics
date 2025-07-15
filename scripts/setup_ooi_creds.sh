# Set your OOINet credentials (make sure to replace API_Username and
# API_Token below with your credentials!!)
cd ~
touch .netrc
chmod 600 .netrc
cat <<EOT >> .netrc
machine ooinet.oceanobservatories.org
login API_Username
password API_Token
EOT