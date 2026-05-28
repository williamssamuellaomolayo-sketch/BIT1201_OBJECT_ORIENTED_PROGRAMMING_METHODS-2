import asyncio
from typing import List, Dict, Optional, Union
from datetime import datetime

# Define the data structure for a Book using type annotations
class Book:
    def __init__(self, book_id: int, title: str, author: str, category: str):
        self.book_id: int = book_id
        self.title: str = title
        self.author: str = author
        self.category: str = category
        self.is_borrowed: bool = False

# Simulated database
library_db: List[Book] = [
    Book(1, "Python Programming", "A.B. Coker", "Technology"),
    Book(2, "Object-Oriented Design", "S.U. Kanu", "Software"),
    Book(3, "Digital Systems", "L. University", "Technology"),
]

# --- Simulated Endpoints ---

async def get_books(query: str) -> List[Dict[str, Union[int, str]]]:
    """
    Simulates GET /books endpoint.
    Searches for books by title, author, or category[cite: 29].
    """
    print(f"[API] Searching for: '{query}'...")
    await asyncio.sleep(1)  # Simulate network/database delay
    
    results = [
        {"id": b.book_id, "title": b.title, "author": b.author}
        for b in library_db
        if query.lower() in b.title.lower() or 
           query.lower() in b.author.lower() or 
           query.lower() in b.category.lower()
    ]
    return results

async def post_borrow(user_name: str, book_id: int) -> Dict[str, str]:
    """
    Simulates POST /borrow endpoint.
    Allows a user to borrow a book[cite: 30].
    """
    print(f"[API] User '{user_name}' is requesting Book ID: {book_id}...")
    await asyncio.sleep(1.5)  # Simulate processing delay
    
    for book in library_db:
        if book.book_id == book_id:
            if not book.is_borrowed:
                book.is_borrowed = True
                return {"status": "success", "message": f"Book '{book.title}' borrowed by {user_name}."}
            return {"status": "error", "message": "Book is already borrowed."}
            
    return {"status": "error", "message": "Book not found."}

# --- Multi-User Simulation ---

async def main():
    print("--- Starting Limkokwing Library API Simulation ---")
    
    # Simulating multiple users accessing the system at the same time [cite: 32]
    tasks = [
        get_books("Technology"),
        post_borrow("Student_A", 1),
        post_borrow("Student_B", 1), # Should fail because Student_A got it first
        post_borrow("Student_C", 2),
    ]
    
    # Run all tasks concurrently
    responses = await asyncio.gather(*tasks)
    
    for i, resp in enumerate(responses):
        print(f"Response {i+1}: {resp}")

if __name__ == "__main__":
    asyncio.run(main())