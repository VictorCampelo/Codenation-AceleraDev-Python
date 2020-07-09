from api.models import User, Agent, Event, Group
from datetime import datetime, timedelta


# Traga todos os uarios ativos, seu último login deve ser menor que 10 dias.
# Retorne a quantidade total de usuarios do sistema.
# Traga todos os usuarios com grupo = 'admin'.
# Traga todos os eventos com tipo debug.
# Traga todos os eventos do tipo critico de um usuário específico.
# Traga todos os agentes de associados a um usuário pelo nome do usuário.
# Traga todos os grupos que contenham alguem que possua um agente que possuem eventos do tipo information.

def get_active_users() -> User:
    return User.objects.filter(last_login__lte=(datetime.today() - timedelta(days=10)))

def get_amount_users() -> User:
    """Retorne a quantidade total de usuarios do sistema """
    return User.objects.count()

def get_admin_users() -> User:
    """Traga todos os usuarios com grupo = 'admin"""
    return User.objects.filter(group__name__contains=('admin'))

def get_all_debug_events() -> Event:
    """Traga todos os eventos com tipo debug"""
    return Event.objects.filter(level='debug')

def get_all_critical_events_by_user(agent) -> Event:
    """Traga todos os eventos do tipo critico de um usuário específico"""
    return Event.objects.filter(agent=agent).filter(level__contains='critical')

def get_all_agents_by_user(username) -> Agent:
    """Traga todos os agentes de associados a um usuário pelo nome do usuário"""
    return Agent.objects.filter(user__name=username)

def get_all_events_by_group() -> Group:
    """Traga todos os grupos que contenham alguem que possua um agente que possuem eventos do tipo information"""
    g = []
    for grp in Group.objects.all():
        for usr in grp.user_set.all():
            for agt in usr.agent_set.all():
                g.append(agt.objects.filter(level__contains='information'))
    return g