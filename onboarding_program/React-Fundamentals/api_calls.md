# Why is it useful to create a reusable Axios instance?

- It ensures consistency since it shares baseURL, headers, and timeout settings across all requests.
- It avoids repeating config in every request, which comply with the DRY principle.
- You can reuse multiple instances for different APIs (user API and product API).
- It is easy to attach request/response interceptors for logging, error handling, or authentication.

## How does intercepting requests help with authentication?

- Interceptors can automatically attach authentication tokens to requests, handle token refresh, and manage errors, improving security by enforcing authentication logic and avoiding duplication across components.

### What happens if an API request times out, and how can you handle it?

- Timeouts occur when a request takes longer than the configured limit. The request is aborted and the user may see a blank screen or spinning sign unless the request is handled properly.
- You can handle it by setting a timeout, catching the error, showing a user-friendly message, and retrying the request.
