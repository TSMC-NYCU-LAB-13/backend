set -a # automatically export all variables
source .env
set +a

if [ "$ENV" = "development" ]; then
    echo "Development mode!"
    exec "$@"
else
    uvicorn main:app
fi

