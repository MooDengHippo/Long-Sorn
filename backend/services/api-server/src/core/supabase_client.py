# @track_context("config.md")

from supabase import Client, create_client

from src.core.config import settings

# Global client instance to preserve PKCE state
_supabase_client: Client | None = None


def get_supabase_client() -> Client:
    """Get Supabase client instance (singleton to preserve PKCE state)"""
    global _supabase_client
    if _supabase_client is None:
        _supabase_client = create_client(settings.SUPABASE_URL, settings.SUPABASE_KEY)
    return _supabase_client
