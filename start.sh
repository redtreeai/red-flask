echo '服务部署成功 端口5000'
nohup gunicorn -c gunicorn_config.py run:app &