# GPIO Web Server

This project is a simple web server built with Flask that allows you to control GPIO pins on a Raspberry Pi. It provides a web interface to switch GPIO pins 18, 17, 15, and 14 on and off.

## Requirements

Before running the application, ensure you have the following installed:

- Python 3
- Flask
- Gunicorn
- RPi.GPIO

You can install the required packages using the provided `requirements.txt` file:

```bash
pip install -r requirements.txt
```

## Running with Flask

To run the webserver with flask, just start the ``app.py`` file with python. (You will probably need root priviliges to start the server on port 80)

```bash
sudo python app.py
```

## Running as a Systemd Service

To run the application as a service using systemd, follow these steps:

1. **Create a Systemd Unit File**

   Create a new systemd service file named `gpio_webserver.service`:

   ```bash
   sudo nano /var/lib/systemd/system/gpio_webserver.service
   ```

   Add the following content to the file, adjusting the paths and user as necessary:

   ```ini
   [Unit]
   Description=GPIO Web Server
   After=network.target

   [Service]
   User=root
   Group=www-data
   WorkingDirectory=/path/to/gpio_webserver  # Change this to your project directory
   ExecStart=/path/to/gunicorn --workers 3 --bind unix:gpio_webserver.sock -m 007 gpio_server:app

   [Install]
   WantedBy=multi-user.target
   ```

2. **Reload Systemd**

   After creating the service file, reload the systemd manager configuration:

   ```bash
   sudo systemctl daemon-reload
   ```

3. **Enable and start the Service**

   Enable the service to start on boot:

   ```bash
   sudo systemctl enable --now gpio_webserver.service
   ```

5. **Check the Service Status**

   You can check the status of the service to ensure it is running:

   ```bash
   sudo systemctl status gpio_webserver.service
   ```

## Accessing the Application

You can access the web interface at `http://<your-raspberry-pi-ip>:8000` (or the port you specified in the Gunicorn command).

## Cleanup

To stop the service and clean up GPIO settings, you can create a shutdown route in your application or manually stop the service:

```bash
sudo systemctl stop gpio_webserver.service
```
