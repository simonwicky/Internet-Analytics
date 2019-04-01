def status_list(MAX_DAYS, epidemic):
    """
    Using a sir, return three lists, containing at index t, a list nodes susceptible/infected/recovered at time t
    """
    list_susceptible = []
    list_infected = []
    list_recovered = []
    for t in range(0,MAX_DAYS):
        cur_susceptible = []
        cur_recovered = []
        cur_infected = []
        for i in range(len(epidemic.inf_time)):  
            if epidemic.inf_time[i] > t:
                cur_susceptible.append(i)
            elif epidemic.rec_time[i] > t:    
                cur_infected.append(i) 
            else:
                cur_recovered.append(i)
        list_infected.append(cur_infected)
        list_susceptible.append(cur_susceptible)
        list_recovered.append(cur_recovered)
        
    return (list_susceptible, list_infected, list_recovered)

def color(G, t, infected, susceptible):
    """
    Take a day t, a list of list of nodes and create a color map to use for a drawing
    """
    color = ['green'] * len(G.nodes)
    for node in G.nodes:
        if node in infected[t]:
            color[node] = 'red'
        elif node in susceptible[t]:
            color[node] = 'blue'
    
    return color