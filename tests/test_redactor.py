from toolkit.redactor import redact_text

def test_redact_ipv4():
    text = "Connected to database at 192.168.1.100 successfully."
    redacted = redact_text(text)
    assert "192.168.1.100" not in redacted
    assert "[REDACTED IPV4]" in redacted

def test_redact_api_key():
    text = "Authorization: Bearer my_super_secret_token_123456789"
    redacted = redact_text(text)
    assert "my_super_secret_token_123456789" not in redacted
    assert "[REDACTED API_KEY]" in redacted

def test_redact_email():
    text = "User admin@example.com logged in."
    redacted = redact_text(text)
    assert "admin@example.com" not in redacted
    assert "[REDACTED EMAIL]" in redacted