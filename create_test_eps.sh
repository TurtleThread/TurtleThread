echo "Building container..."
docker build -t turtlethread .
echo "Starting container..."
docker run -d -t --name "genps" turtlethread
echo "Creating postscript..."
docker exec genps bash -c "cd turtlethread && python3 tests/create_postscript.py"
echo "Copying postscript..."
docker cp genps:/turtlethread/tests/visualise_postscript tests/
echo "Cleanup..."
docker kill genps
docker rm genps