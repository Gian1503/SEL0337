[Unit]
Description=Blink LED 
After=multi-user.target

[Service]
ExecStart=/usr/bin/python3 /home/sel/blink.py
ExecStop=/usr/bin/python3 /home/sel/stop_blink.py
User=sel

[Install]
WantedBy=multi-user.target
