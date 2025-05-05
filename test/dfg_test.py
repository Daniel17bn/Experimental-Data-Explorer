from xes_dfg import xes_dfg

def test_xes_dfg():
    # Path to the test XES file
    xes_path = r"C:\Users\danie\OneDrive - University of Luxembourg\BSP\backend\data\xes\example.xes"
    
    # Call the xes_dfg function
    try:
        result = xes_dfg(xes_path)
        print("Test Passed!")
        print("Result:")
        print(result)
    except Exception as e:
        print("Test Failed!")
        print(f"Error: {e}")

# Run the test
if __name__ == "__main__":
    test_xes_dfg()