# Seldon with titanic dataset 

## Dataset
<hr/>


https://www.kaggle.com/c/titanic


<br>

## Folder Architecture
<hr/>
<ul>
    
<li> <ins> <strong>data</strong> </ins> :  Data of the dataset </li>

<li> <ins> <strong>model</strong> </ins> :  Contains the different scaler / model and 
    transformers </li>

<li> <ins> <strong>notebook</strong> </ins> : titanic notebook, and seldon core  </li>

<li> <ins> <strong>seldon</strong> </ins> :  Seldon Configuration files</li>
</ul>
</br>

## Environment
<hr>

create your environment (I use conda): 
    <ul>
        <li> <code>conda create -n  name python=3.8 </code></li>
        <li> <code> pip install -r seldon/requirement.txt</code></li>
    </ul>
</br>
## Installation
<hr>

Seldon Installation and configuration (localy) : https://docs.seldon.io/projects/seldon-core/en/latest/install/kind.html

<ins> NB: </ins> Seldon works well with kubernetes 1.24 to create kind cluster use this command 
<code>  
kind create cluster --name seldon --image kindest/node:v1.24.7@sha256:577c630ce8e509131eab1aea12c022190978dd2f745aac5eb1fe65c0807eb315
</code>
and then follow the steps in the documentation

</br>

## Code setup and config
<hr>
<ol>
<li> Build Docker Image with python3.8 seldon: <code> docker build . -f Dockerfile -t seldonio/seldon-core-titanic:1.4</code>
<li> Use s2i to build docker image with required files and config required by seldon: <code> s2i build . seldonio/seldon-core-titanic:0.4  seldonio/titanic:1.4 </code>
<li> Load image into kind: <code> kind load docker-image seldonio/titanic:1.4 --name seldon </code></li>
<li> Apply Seldon Deployment yml file: <code>kubectl apply -f sdpl.yml</code></li>
<li> Check if pod running: <code> kubectl get pods</code></li>
<li> Port Forwarding: <code> kubectl port-forward -n istio-system svc/istio-ingressgateway 8081:80 </code>
<li> Run seldon notebook
</ol>
