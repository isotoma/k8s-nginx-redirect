FROM nginx:alpine
RUN apk add --no-cache python3 py3-yaml
RUN mkdir /etc/nginx-redirect
VOLUME /etc/nginx-redirect
COPY entry-point.py /entry-point.py
RUN chmod +x /entry-point.py
ENTRYPOINT /entry-point.py
