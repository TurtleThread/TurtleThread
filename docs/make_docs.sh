echo "Building container..."
docker build -t turtlethread ..
echo "Starting container..."
docker run -d -t --name "turtlethread_docs" turtlethread
echo "Building documentation..."
docker exec turtlethread_docs bash -c "cd turtlethread/docs && make clean html"
echo "Copying build artifacts..."
docker cp turtlethread_docs:/turtlethread/docs/_build .
echo "Cleanup..."
docker kill turtlethread_docs
docker rm turtlethread_docs