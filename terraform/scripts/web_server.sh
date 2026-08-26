#!/bin/bash

# Update the server
apt-get update -y

# Install Apache Web Server
apt-get install -y apache2

# Enable Apache
systemctl enable apache2
systemctl start apache2

# Create the website homepage
cat <<EOF > /var/www/html/index.html
<!DOCTYPE html>
<html>
<head>
    <title>CloudOps ServiceDesk</title>
</head>
<body style="font-family:Arial;text-align:center;margin-top:60px;">
    <h1>CloudOps ServiceDesk</h1>
    <h2>Infrastructure deployed successfully using Terraform</h2>
    <p>This web server was automatically provisioned through Infrastructure as Code (IaC).</p>
</body>
</html>
EOF

# Restart Apache
systemctl restart apache2