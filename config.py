# config.py - ONLY config here, no routes!
from supabase import create_client

SUPABASE_URL = "https://zqbcjfcximpndjugqbnt.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InpxYmNqZmN4aW1wbmRqdWdxYm50Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzMyMzk5NTIsImV4cCI6MjA4ODgxNTk1Mn0.FQ0rXbOmiQB7AC4k4gOfeVBzmKgYGHYflcwzP9OPvGM"

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)