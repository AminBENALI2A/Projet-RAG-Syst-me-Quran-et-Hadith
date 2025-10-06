import requests

def query_vector_base(arabic_query,vector_base):
    # API endpoint
    url = "https://8139-34-87-183-115.ngrok-free.app/query" #coller le URL générer par ngrok ici +/query

    # Request payload
    payload = {
        "vector_base": vector_base,
        "query": arabic_query
    }

    # Headers
    headers = {
        "Content-Type": "application/json"
    }

    # Send POST request
    response = requests.post(url, json=payload, headers=headers)
    print(response)

    # Check response and return results
    if response.status_code == 200:
        #{"generated": final_results, "retrieved": decoded_text()}
        return response.json()["generated"], response.json()["retrieved"]
    else:
        raise Exception(f"Failed to query vector base. Status code: {response.status_code}, Error: {response.text}")

