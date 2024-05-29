
# Import for the Web Bot
from botcity.web import WebBot, Browser, By

# Import for integration with BotCity Maestro SDK
from botcity.maestro import *
from webdriver_manager.chrome import ChromeDriverManager

# Disable errors if we are not connected to Maestro
BotMaestroSDK.RAISE_NOT_CONNECTED = False

class Bot(WebBot):

    lista_livros = [
        'Dom casmurro', 
        'Memórias Póstumas de Brás Cubas', 
        'Vidas Secas',
        'O Cortiço',
        'Capitães da Areia',
        'Iracema',
        'Senhora',
        'A Moreninha',
        'Morte e Vida Severina',
        'O Auto da Compadecida'
        ]

    def buscar_livro(self, livro):
        self.find_element('auto-complete', By.ID).send_keys(livro)
        self.enter()


    def entrar_pagina_livro(self):
        #Encontro o livro e entro na pagina dele
        livros = self.find_elements('listagem-item-wrap', By.CLASS_NAME)
        link = livros[0].find_element_by_tag_name('a').get_attribute('href')
        for livro in livros[:1]:
            livro
            livro.click()
        
        return link

    def extrair_informacoes_livro(self):
        #Extrair informações do livro 
        #titulo
        titulo = self.find_element('//*[@id="corpo"]/div[1]/div/div[2]/div/div/div[2]/div/div[1]/h1', By.XPATH).text
        #preco
        preco = self.find_element('//*[@id="corpo"]/div[1]/div/div[2]/div/div/div[2]/div/div[2]/div[1]/div/div[1]/strong',By.XPATH).text
        
        #autor
        autor = self.find_element('//*[@id="descricao"]/ul/li[1]', By.XPATH).text
        autor  = autor.split(':')
        autor = autor[2]
        #Editora
        editora = self.find_element('//*[@id="descricao"]/ul/li[2]', By.XPATH).text
        editora = editora.split(':')
        editora = editora[1]
        #qtd_paginas
        qtd_paginas = self.find_element('//*[@id="descricao"]/ul/li[4]', By.XPATH).text
        qtd_paginas = qtd_paginas.split(':')
        qtd_paginas = qtd_paginas[1]

    

        return titulo,preco,autor,editora,qtd_paginas

    def action(self, execution):
        # Runner passes the server url, the id of the task being executed,
        # the access token and the parameters that this task receives (when applicable).
        maestro = BotMaestroSDK.from_sys_args()
        ## Fetch the BotExecution with details from the task, including parameters
        execution = maestro.get_execution()

        print(f"Task ID is: {execution.task_id}")
        print(f"Task Parameters are: {execution.parameters}")


        # Configure whether or not to run on headless mode
        self.headless = False

        # Uncomment to change the default Browser to Firefox
        self.browser = Browser.CHROME

        # Uncomment to set the WebDriver path
        self.driver_path = ChromeDriverManager().install()

        # Opens the BotCity website.
        self.browse("https://www.livroselivros.com.br")

        #Maximizar Janela
        self.maximize_window()


        # Implement here your logic...
        try:

            for livro in self.lista_livros:
                self.buscar_livro(livro)
                link_livro = self.entrar_pagina_livro()
                self.wait(1000)
                titulo,preco,autor,editora,qtd_paginas = self.extrair_informacoes_livro()


                print(f'Titulo {titulo}')
                print(f'link do livro {link_livro}')
                print(f'Preço {preco}')
                print(f'Autor {autor}')
                print(f'editora {editora}')
                print(f'Quantidade de paginas {qtd_paginas}')
                self.navigate_to('https://www.livroselivros.com.br')
            

        except Exception as ex:
            print(ex)
        finally:
            # Wait 3 seconds before closing
            self.wait(3000)

            # Finish and clean up the Web Browser
            # You MUST invoke the stop_browser to avoid
            # leaving instances of the webdriver open
            self.stop_browser()

            # Uncomment to mark this task as finished on BotMaestro
            maestro.finish_task(
                task_id=execution.task_id,
                status=AutomationTaskFinishStatus.SUCCESS,
                message="Tarefa Finalizada com sucesso"
            )


    def not_found(label):
        print(f"Element not found: {label}")


if __name__ == '__main__':
    Bot.main()
