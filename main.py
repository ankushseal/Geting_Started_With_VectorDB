from qdrant_client import models, QdrantClient
from sentence_transformers import SentenceTransformer

encoder = SentenceTransformer("all-MiniLM-L6-v2")

with open('HC_data.json', 'r') as file:
    # Read the content of the file
    file_content = file.read()

documents = [
  {
    "memberid": "M001",
    "member_name": "John Doe",
    "covg_start_date": "2023-01-01",
    "covg_end_date": "2023-12-31",
    "address": "123 Main Street",
    "city": "Anytown",
    "dob": "1980-05-15"
  },
  {
    "memberid": "M002",
    "member_name": "Jane Smith",
    "covg_start_date": "2023-02-15",
    "covg_end_date": "2023-11-30",
    "address": "456 Oak Avenue",
    "city": "Sometown",
    "dob": "1992-08-20"
  },
  {
    "memberid": "M003",
    "member_name": "Bob Johnson",
    "covg_start_date": "2023-03-10",
    "covg_end_date": "2023-10-15",
    "address": "789 Pine Road",
    "city": "Othercity",
    "dob": "1975-11-03"
  },
  {
    "memberid": "M004",
    "member_name": "Alice Brown",
    "covg_start_date": "2023-04-22",
    "covg_end_date": "2023-09-28",
    "address": "101 Cedar Lane",
    "city": "Cityville",
    "dob": "1988-02-18"
  },
  {
    "memberid": "M005",
    "member_name": "Charlie Wilson",
    "covg_start_date": "2023-05-07",
    "covg_end_date": "2023-08-20",
    "address": "202 Elm Street",
    "city": "Villagetown",
    "dob": "1995-06-25"
  },
  {
    "memberid": "M006",
    "member_name": "Eva Martinez",
    "covg_start_date": "2023-06-30",
    "covg_end_date": "2023-07-31",
    "address": "303 Maple Avenue",
    "city": "Smallville",
    "dob": "1983-09-12"
  },
  {
    "memberid": "M007",
    "member_name": "David Lee",
    "covg_start_date": "2023-07-15",
    "covg_end_date": "2023-06-30",
    "address": "404 Birch Road",
    "city": "Metrocity",
    "dob": "1970-04-08"
  },
  {
    "memberid": "M008",
    "member_name": "Grace Taylor",
    "covg_start_date": "2023-08-18",
    "covg_end_date": "2023-05-25",
    "address": "505 Walnut Lane",
    "city": "Suburbia",
    "dob": "1990-12-01"
  },
  {
    "memberid": "M009",
    "member_name": "Frank White",
    "covg_start_date": "2023-09-05",
    "covg_end_date": "2023-04-15",
    "address": "606 Pine Street",
    "city": "Uptown",
    "dob": "1990-12-01"
  },
  {
    "memberid": "M010",
    "member_name": "Holly Adams",
    "covg_start_date": "2023-10-12",
    "covg_end_date": "2023-03-20",
    "address": "707 Oak Lane",
    "city": "Downtown",
    "dob": "1978-03-28"
  }
]


qdrant = QdrantClient(":memory:")

qdrant.recreate_collection(
    collection_name="HC_data",
    vectors_config=models.VectorParams(
        size=encoder.get_sentence_embedding_dimension(),  # Vector size is defined by used model
        distance=models.Distance.COSINE,
    ),
)

qdrant.upload_records(
    collection_name="HC_data",
    records=[
        models.Record(
            id=idx, vector=encoder.encode(doc["dob"]).tolist(), payload=doc
        )
        for idx, doc in enumerate(documents)
    ],
)
hits = qdrant.search(
    collection_name="HC_data",
    query_vector=encoder.encode(input("Enter the DOB which you want to search : ")).tolist(),
    #limit=1,
)
distance = hits[0].score
for hit in hits:
  if distance == hit.score:
    print(hit.payload, "score:", hit.score)