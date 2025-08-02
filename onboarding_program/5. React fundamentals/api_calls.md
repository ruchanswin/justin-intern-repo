# Why is it useful to create a reusable Axios instance?
 It centralizes configuration (base URL, headers, interceptors), reduces code duplication, and makes it easier to update settings for all requests in one place.

# How does intercepting requests help with authentication?
 Interceptors can automatically attach authentication tokens to requests, handle token refresh, and manage errors, improving security and reducing repetitive code.

# What happens if an API request times out, and how can you handle it?
 If a request times out, the client receives an error. You can handle it by setting a timeout, catching the error, showing a user-friendly message, and optionally retrying the request.