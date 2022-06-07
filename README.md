# backend

## 部署步驟

- 建立 ns 與 secret
  
    ```sh
    kubectl create -n tsmc-nycu-lab-13 secret generic backend-env --from-env-file=.env
    ```

- 部署

    ```sh
    kubectl apply -k kustomize-backend
    ```
