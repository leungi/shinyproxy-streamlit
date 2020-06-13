# Credits
- [Shinyproxy](https://github.com/openanalytics/shinyproxy)
- [Streamlit](https://github.com/streamlit/streamlit)

# Running `streamlit` image inside ShinyProxy 

[Streamlit](https://www.streamlit.io/) is a Shiny-like app development library for Python.

[ShinyProxy](https://www.shinyproxy.io/) is a deployment platform built for Shiny, and extendable to other apps.

To build the image from the Dockerfile, clone this repo with `git clone https://github.com/leungi/shinyproxy-streamlit.git`.

Navigate into the repo and run

```
sudo docker build -t shinyproxy-streamlit .
```

For deployment on ShinyProxy, include the below in the `specs` section of `application.yml` configuration file.

If running ShinyProxy as installed .rpm (e.g., RHEL), note that the `application.yml` may be located in `/etc/shinyproxy/application.yml`.

If running as .jar (e.g., shinyproxy-2.3.0.jar), then the `application.yml` should be placed in same folder as .jar file.

For more info, visit [ShinyProxy config](https://www.shinyproxy.io/configuration/).

```
specs:
  - id: streamlit
    display-name: Demo Streamlit app
    description: Adding another non shiny app to shinyproxy
    container-cmd: ["streamlit", "run", "app.py", "--server.port=8501"]
    container-image: shinyproxy-streamlit
    # Streamlit runs on port 8501
    port: 8501
```
