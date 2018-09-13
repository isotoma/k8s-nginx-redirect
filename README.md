# k8s-nginx-redirect

A pod that configures and then runs nginx based on redirect specifications
delivered in a chart configuration.

An example configuration would look like the following in values:

    hosts: []
    - host: foo.example.com
    patterns:
    - from: "^/$"
        to: "https://bar.example.com/"
    - from: "^/([^/]+)$"
        to: "https://$1.example.com/"

This then configures both the ingress and the nginx redirection configuration.

