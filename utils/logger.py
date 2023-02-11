from datetime import datetime
from blockchain.main import blockchain_connection

class Logger():
    def __init__(self, type):
        self.logger_type = type
        self.app_name = "APP_RU"
        self.blockchain_connection = blockchain_connection
    
    def log(self, user, user_interaction):
        formatted_log = self.format_log(user, user_interaction)
        receipt = self.blockchain_connection.create_item(user["id"], formatted_log)
        return receipt
    
    def format_log(self, user, interaction):
        action_description = self.get_interaction_description(interaction)
        
        # 2023-12-31 12:00:00   APP:action | User Luiz performed a Pix payment
        log_message = f"{datetime.today().strftime('%Y-%m-%d %H:%M:%S')} {self.app_name}:{self.logger_type} | User {user.get('name')} [{user['id']}] {action_description}"
        return log_message

    def get_interaction_description(self, interaction):
        if interaction == UserInteractions.LOGIN:
            return "logged in"
        elif interaction == UserInteractions.LOGOFF:
            return "logged off"

        elif interaction == UserInteractions.VIEW_DATA:
            return "viewed their data"
        elif interaction == UserInteractions.VIEW_TICKET_LIST:
            return "viewed their ticket list"
        elif interaction == UserInteractions.VIEW_TICKET_HISTORY:
            return "viewed their ticket history"
        elif interaction == UserInteractions.VIEW_FOOD_MENU:
            return "viewed the food menu"

        elif interaction == UserInteractions.BUY_TICKET:
            return "bought a ticket"
        elif interaction == UserInteractions.SELECT_TICKET:
            return "selected a ticket for consumption"
        elif interaction == UserInteractions.PIX_PAYMENT:
            return "payed a ticket with Pix"
            
        
class UserInteractions():
    LOGIN = 1
    LOGOFF = 2
    VIEW_DATA = 3
    VIEW_TICKET_LIST = 4
    VIEW_TICKET_HISTORY = 5
    VIEW_FOOD_MENU = 6
    BUY_TICKET = 7
    SELECT_TICKET = 8
    PIX_PAYMENT = 9



'''
RF03 Visualizar dados da carteirinha, curso e unidade.
permite que os usuários visualizem informações da carteirinha, do curso, da
unidade e demais informações caso estejam logados.

RF04 Visualizar lista de tickets
permite que os usuários logados visualizem a sua lista de tickets, exibindo
quantidade de tickets e a qual tipo de refeição esse ticket pertence.

RF05 Visualizar cardápio.
permite que usuários logados vejam o cardápio referente ao dia da semana e a
unidade de ensino da UEA o qual desejar.

RF05 Visualizar histórico de uso de tickets.
permite aos usuários logados que visualizem os tickets que foram utilizados,
em qual refeição, o horario que foi utilizado e a unidade de ensino da UEA.


'''

'''
OFF >> RF06 Registrar comentário.
após seja feito a leitura do ticket selecionado previamente, será possível o
registro de um comentário referente aquele ticket utilizado.

OFF >> RF06 Compartilhar Tickets com um amigo
Permite que um usuário compartilhe um de seus tickets de uma determinada
refeição com outro usuário.

RF06 Comprar tickets.
permite ao usuário quando logado efetuar compra prévia de uma certa quan-
tidade de tickets de uma determinada refeição.

RF07 Selecionar ticket para consumo.
permite que o usuário emita um QR Code de um ticket referente a uma
refeição em especı́fico para que este seja debitado após leitura por parte do sis-
tema do RU o qual é o mesmo da API da UEA.

RF08 Efetuar pagamento via PIX.
permite que o usuário finalize a compra dos tickets após concluir o pagamento
utilizando o PIX, tendo assim os tickets creditados ao seu usuário.
'''

'''
RF01 Efetuar Login no aplicativo.
usuário efetua o login na aplicação na qual suas credenciais são validadas pela
API do Google no Front-end.

RF02 Efetuar Logoff do aplicativo.
os usuários podem sair da aplicação.
'''