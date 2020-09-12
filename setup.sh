mkdir -p ~/.streamlit/
echo "\
[general]\n\
email = \"f20170088@goa.bits-pilani.ac.in\"\n\
" > ~/.streamlit/credentials.toml
echo "\
[server]\n\
headless = true\n\
enableCORS=false\n\
port = $PORT\n\
" > ~/.streamlit/config.toml
