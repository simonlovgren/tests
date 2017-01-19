.PHONY: %.cpp
%: %.cpp
	g++ -fopenmp -o bin/$@ $^
	@echo "-------------------\n"
	@./bin/$@
	@echo ""
