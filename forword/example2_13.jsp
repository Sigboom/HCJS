<%@ page contentType="text/html;charset=utf-8"%>
<html>
    <body>
        <% double i = Math.random();
        %>
        <jsp:forward page="come.jsp">
        <jsp:param name="number" value="<%=i%>"/>
        </jsp:forward>
        hhhh
    </body>
</html>
