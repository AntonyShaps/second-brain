from fastapi import FastAPI

app = FastAPI()

@app.get("/")

def root():
    return {"message" : " heee" }


if __name__ == "__main__":
    main()
