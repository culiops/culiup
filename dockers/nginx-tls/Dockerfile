FROM nginx:1.20.2-alpine

RUN apk add --no-cache ca-certificates openssl

RUN openssl req -x509 -nodes -days 365 -subj "/C=CA/ST=QC/O=culiops, Inc./CN=dev.culiops.xyz" \
    -newkey rsa:2048 -keyout /etc/ssl/private/nginx-selfsigned.key -out /etc/ssl/certs/nginx-selfsigned.crt;
 
ADD scripts/docker-entrypoint.sh /docker-entrypoint.sh
RUN chmod +x /docker-entrypoint.sh

ENTRYPOINT ["/docker-entrypoint.sh"]
